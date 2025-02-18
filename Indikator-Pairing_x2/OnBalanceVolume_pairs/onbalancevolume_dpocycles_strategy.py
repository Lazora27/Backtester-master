import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und DPOCycles
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'DPOCycles': 1.0
        })
    )
