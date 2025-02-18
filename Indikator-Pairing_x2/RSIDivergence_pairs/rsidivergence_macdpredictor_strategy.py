import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MACDPredictor': 1.0
        })
    )
