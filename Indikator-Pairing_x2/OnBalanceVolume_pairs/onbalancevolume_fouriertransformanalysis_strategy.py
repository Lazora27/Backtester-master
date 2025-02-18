import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
