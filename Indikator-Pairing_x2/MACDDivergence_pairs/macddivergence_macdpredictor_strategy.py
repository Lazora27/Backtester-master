import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MACDPredictor': 1.0
        })
    )
