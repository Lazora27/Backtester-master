import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
