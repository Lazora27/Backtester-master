import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
