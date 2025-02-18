import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
