import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
