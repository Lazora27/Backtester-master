import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
