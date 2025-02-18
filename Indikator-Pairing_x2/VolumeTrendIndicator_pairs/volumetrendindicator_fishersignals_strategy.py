import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
