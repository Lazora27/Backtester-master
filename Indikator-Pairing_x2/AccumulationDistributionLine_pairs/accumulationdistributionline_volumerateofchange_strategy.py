import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
