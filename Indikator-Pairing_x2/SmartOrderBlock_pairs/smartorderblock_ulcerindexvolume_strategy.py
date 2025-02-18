import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
