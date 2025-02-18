import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
