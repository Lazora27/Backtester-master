import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
