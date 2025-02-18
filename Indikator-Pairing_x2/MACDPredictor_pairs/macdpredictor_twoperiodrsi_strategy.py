import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
