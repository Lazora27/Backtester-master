import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
