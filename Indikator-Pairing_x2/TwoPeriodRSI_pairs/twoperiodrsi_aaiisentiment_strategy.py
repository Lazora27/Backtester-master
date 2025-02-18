import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AAIISentiment': 1.0
        })
    )
