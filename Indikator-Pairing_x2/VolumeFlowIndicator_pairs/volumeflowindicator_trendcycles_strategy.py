import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
