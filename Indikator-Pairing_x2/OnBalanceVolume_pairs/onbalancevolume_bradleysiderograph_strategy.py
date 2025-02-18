import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'BradleySiderograph': 1.0
        })
    )
