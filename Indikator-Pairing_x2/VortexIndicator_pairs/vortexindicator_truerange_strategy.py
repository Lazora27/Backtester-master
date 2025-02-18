import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
