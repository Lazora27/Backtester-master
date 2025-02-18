import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AAIISentiment': 1.0
        })
    )
