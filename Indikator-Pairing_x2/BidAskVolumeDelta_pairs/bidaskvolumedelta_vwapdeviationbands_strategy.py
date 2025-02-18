import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
