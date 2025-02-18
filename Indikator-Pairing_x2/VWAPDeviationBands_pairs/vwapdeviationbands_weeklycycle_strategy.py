import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'WeeklyCycle': 1.0
        })
    )
