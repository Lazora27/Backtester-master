import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und MassIndex
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'MassIndex': 1.0
        })
    )
