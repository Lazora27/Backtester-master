import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
