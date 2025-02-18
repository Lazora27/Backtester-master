import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
