import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
