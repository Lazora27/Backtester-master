import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FisherSignals': 1.0
        })
    )
