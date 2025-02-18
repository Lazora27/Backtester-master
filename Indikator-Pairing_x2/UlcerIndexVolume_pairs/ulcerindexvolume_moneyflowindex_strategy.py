import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
