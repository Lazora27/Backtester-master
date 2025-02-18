import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
