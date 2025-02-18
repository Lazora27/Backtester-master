import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
