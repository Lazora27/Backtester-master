import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
