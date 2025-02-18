import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VortexIndicator': 1.0
        })
    )
