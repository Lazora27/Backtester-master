import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'VortexIndicator': 1.0
        })
    )
