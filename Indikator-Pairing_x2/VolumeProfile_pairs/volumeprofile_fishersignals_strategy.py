import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FisherSignals': 1.0
        })
    )
