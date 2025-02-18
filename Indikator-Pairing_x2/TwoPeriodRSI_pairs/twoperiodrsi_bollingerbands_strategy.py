import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
