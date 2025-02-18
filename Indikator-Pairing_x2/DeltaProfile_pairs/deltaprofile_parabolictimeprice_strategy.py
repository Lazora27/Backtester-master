import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
