import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ModifiedRSI': 1.0
        })
    )
