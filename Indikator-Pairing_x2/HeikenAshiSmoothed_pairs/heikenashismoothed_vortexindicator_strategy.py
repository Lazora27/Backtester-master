import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiSmoothed_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiSmoothed und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'HeikenAshiSmoothed': 1.0,
            'VortexIndicator': 1.0
        })
    )
