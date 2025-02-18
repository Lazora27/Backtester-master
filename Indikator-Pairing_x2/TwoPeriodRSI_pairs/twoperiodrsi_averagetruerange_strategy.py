import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
