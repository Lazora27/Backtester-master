import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und FisherSignals
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'FisherSignals': 1.0
        })
    )
