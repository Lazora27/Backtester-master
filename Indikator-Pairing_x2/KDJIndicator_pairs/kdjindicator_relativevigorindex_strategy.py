import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
