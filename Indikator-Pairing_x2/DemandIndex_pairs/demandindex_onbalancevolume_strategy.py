import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
