import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AroonIndicator': 1.0
        })
    )
