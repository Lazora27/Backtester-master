import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AAIISentiment': 1.0
        })
    )
