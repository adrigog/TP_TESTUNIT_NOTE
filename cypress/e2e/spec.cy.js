describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8501/')
    cy.get('input').eq(0).clear().type('200').type('enter')
    cy.get('input').eq(1).clear().type('3').type('enter')
    cy.get('input').eq(2).clear().type('1').type('enter')

  }
  
  
  
  )



})