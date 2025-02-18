import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und FisherSignals
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'FisherSignals': 1.0
        })
    )
