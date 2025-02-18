import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
