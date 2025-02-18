import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
