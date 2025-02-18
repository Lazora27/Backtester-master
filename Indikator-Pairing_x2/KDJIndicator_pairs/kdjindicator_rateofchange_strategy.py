import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'RateOfChange': 1.0
        })
    )
