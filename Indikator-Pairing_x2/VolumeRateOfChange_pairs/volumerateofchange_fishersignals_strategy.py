import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'FisherSignals': 1.0
        })
    )
