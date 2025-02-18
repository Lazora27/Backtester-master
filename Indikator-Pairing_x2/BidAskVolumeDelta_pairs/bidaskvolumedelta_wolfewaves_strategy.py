import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'WolfeWaves': 1.0
        })
    )
