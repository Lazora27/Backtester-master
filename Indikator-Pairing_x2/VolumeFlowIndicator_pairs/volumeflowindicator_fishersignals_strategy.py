import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
